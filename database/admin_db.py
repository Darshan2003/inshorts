from fastapi_sqlalchemy import db

from database.models import Shorts as ShortsModel
from database.schema import CreateShorts

def create_shorts(shorts: CreateShorts)->int:
    shorts = ShortsModel(
        category = shorts.category,
        title = shorts.title,
        author = shorts.author,
        publish_date = shorts.publish_date,
        content = shorts.content,
        actual_content_link = shorts.actual_content_link,
        image = shorts.image,
        upvote = shorts.vote.upvote,
        downvote = shorts.vote.downvote
    )
    db.session.add(shorts)
    db.session.commit()
    return shorts.short_id
