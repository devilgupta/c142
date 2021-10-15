from flask import Flask,jsonify,request
from storage import all_movies,liked_movies,unliked_movies,did_not_watch_movies
from demographic_filtering import output
from content_filtering import get_recommendations
app=Flask(__name__)

@app.route("/get-movie")
def get_movies():
    movie_data={
        "title":all_movies[0][19],
       # "poster_link":all_movies[0][27],
        "release_date":all_movies[0][13],
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9],
    }
    return jsonify({
        "data":movie_data,
        "status":"success"
    })
@app.route("/liked-movie",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    #all_movies=all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    })
@app.route("/unliked-movie",methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    #all_movies=all_movies[1:]
    unliked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    })
@app.route("/did-not-watch-movie",methods=["POST"])
def did_not_watch_movie():
    movie=all_movies[0]
    #all_movies=all_movies[1:]
    did_not_watch_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"success"
    })

@app.route("/popular-movie")
def popular_movies():
    movie_data=[]
    for movie in output:
        _d={
            "title":movie[0],
            "poster_link":movie[1],
            "release_date":movie[2],
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5],
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    })
@app.route("/recommended-movie")
def recommended_movies():
    all_recommended=[]
    for liked_movie in liked_movies:
        output=get_recommendations(liked_movies[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended=list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data=[]
    for recommended in all_recommended:
        _d={
            "title":recommended[0],
            "poster_link":recommended[1],
            "release_date":recommended[2],
            "duration":recommended[3],
            "rating":recommended[4],
            "overview":recommended[5],
        }
        movie_data.append(_d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    })
if __name__=="__main__":
    app.run()

