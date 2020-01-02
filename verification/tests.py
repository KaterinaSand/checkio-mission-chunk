"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[5,4,7,3,4,5,4], 3],
            "answer": [[5,4,7], [3,4,5], [4]],
        },
        {
            "input": [[3,4,5], 1],
            "answer": [[3], [4], [5]]
        },
        {
            "input": [[5,4], 7],
            "answer": [[5,4],],
        },
        {
            "input": [[], 3],
            "answer": [],
        },
        {
            "input": [[4,4,4,4,], 4],
            "answer": [[4,4,4,4]]
        },
    ],
    "Extra": [
        {
            "input": [[1,2,3], 2],
            "answer": [[1,2], [3]]
        },
        {
            "input": [[1,1,1,1,1], 9],
            "answer": [[1,1,1,1,1]],
        }
    ]
}
