
# def get_news_query_set(query=None):
#     # if this is a POST request we need to process the form data

#     queryset = []
#     queries = query.split(' ')
#     for query in queries:
#         posts = Article.objects.filter(
#             Q(title__icontains=query) |
#             Q(body__icontains=query)
#         ).distinct()

#         for post in posts:
#             queryset.append(post)
#     return list(set(queryset))
