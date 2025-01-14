from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Literal
from datetime import datetime

app = FastAPI()

class CommentInput(BaseModel):
    text: str
    category: Literal["positive", "negative"]

class Comment(BaseModel):
    id: int | None = None
    text: str
    category: Literal["positive", "negative"]
    created_at: datetime | None = None

comments: list[Comment] = [
    Comment(id=0, text="Каждый день я взаимодействовала с потрясающим комьюнити, общалась с единомышленниками и постоянно улучшала свои знания. Курс дал мне не только технические навыки, но и уверенность в своих силах и компетенциях.", category="positive", created_at=datetime(2025, 1, 10, 14, 0, 0)),
    Comment(id=1, text="То, что мы проходили на курсах, помогло пройти техническое собеседование и получить оффер на работу.", category="positive", created_at=datetime(2025, 1, 10, 14, 5, 0)),
    Comment(id=2, text="При обучении очень часто кажется, что не так уж умен!", category="negative", created_at=datetime(2025, 1, 10, 14, 10, 0)),
    Comment(id=3, text="Без знаний менторов я была абсолютным нулем в iOS-разработке. После курса я устроилась на работу, и меня оценили как сильного джуниора.", category="positive", created_at=datetime(2025, 1, 10, 15, 5, 0)),
    Comment(id=4, text="nFactorial-да алған білім жұмысқа тұрардың алдындағы интервью кезінде өте қатты көмектесті. Сол үшін nFactorial ұжымына үлкен алғысымды білдіремін.", category="positive", created_at=datetime(2025, 1, 11, 10, 1, 0)),
]

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>VoxPop</title>
        </head>
        <body>
            <h1>Welcome to VoxPop</h1>
            <a href="/comments">View Comments</a>
        </body>
    </html>
    """

@app.get("/comments", response_class=HTMLResponse)
def get_comments_html(page: int = 1, limit: int = 3):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page and limit must be positive integers")

    start = (page - 1) * limit
    end = start + limit
    paginated_comments = list(reversed(comments))[start:end]

    html_content = """
    <html>
        <head>
            <title>Comments</title>
        </head>
        <body>
            <h1>Public Comments</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Text</th>
                        <th>Category</th>
                        <th>Created At</th>
                    </tr>
                </thead>
                <tbody>
    """

    for comment in paginated_comments:
        html_content += f"""
        <tr>
            <td>{comment.id}</td>
            <td>{comment.text}</td>
            <td>{comment.category}</td>
            <td>{comment.created_at.strftime('%Y-%m-%d %H:%M:%S') if comment.created_at else 'N/A'}</td>
        </tr>
        """

    html_content += """
                </tbody>
            </table>
            <br>
            <a href="/comments?page={prev_page}&limit={limit}">Previous</a>
            <a href="/comments?page={next_page}&limit={limit}">Next</a>
        </body>
    </html>
    """.format(
        prev_page=max(1, page - 1), next_page=page + 1, limit=limit
    )

    return html_content

@app.post("/comments", status_code = 201)
#Creating new comment
def create_comment(comment_input: CommentInput):
    new_comment = Comment(
        id=comments[-1].id + 1 if comments else 0,
        text=comment_input.text,
        category=comment_input.category,
        created_at = datetime.now(),
    )
    comments.append(new_comment)
    return new_comment

@app.get("/comments")
#All comments
def get_comments(page: int = 1, limit: int = 3) -> list[Comment]:
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page and limit must be positive integers")
    start = (page - 1) * limit
    end = start + limit # 3
    return list(reversed(comments))[start:end]

@app.get("/comments/{category}")
#Filter comments by category
def get_all_comments_by_category(category: Literal["positive", "negative"], page: int = 1, limit: int = 3) -> list[Comment]:
    category_comments = list(reversed([comment for comment in comments if comment.category == category]))
    start = (page - 1) * limit
    end = start + limit # 3
    return category_comments[start:end]