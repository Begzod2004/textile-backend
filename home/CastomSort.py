class CustomAPISorter:
    def sort_apis(self, api_list):
        sorted_apis = sorted(api_list, key=lambda api: api.pattern._route)
        return sorted_apis