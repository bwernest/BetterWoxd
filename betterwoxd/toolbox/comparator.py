"""___Modules_______________________________________________________________"""

"""___Classes_______________________________________________________________"""

class Comparator:

    def get_individual_stats(self, data: dict) -> dict:
        return {
            "total_films": len(data.get("films", [])),
            "average_rating": sum(film.get("rating", 0) for film in data.get("films", [])) / max(len(data.get("films", [])), 1)
        }

    def get_duo_stats(self, data1: dict, data2: dict) -> dict:
        return {
        }

    def compare(self, data1: dict, data2: dict) -> dict:
        films_user1 = data1.get("films", [])
        films_user2 = data2.get("films", [])
        return {
            "common_films": self.get_common_films(films_user1, films_user2)
        }

    def get_common_films(self, films1: list, films2: list) -> list:
        titles1 = {film["title"] for film in films1}
        titles2 = {film["title"] for film in films2}
        common_titles = titles1.intersection(titles2)
        return [film for film in films1 if film["title"] in common_titles]
