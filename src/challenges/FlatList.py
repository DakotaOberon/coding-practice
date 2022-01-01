from src.Challenge import Challenge


class FlatList(Challenge):
    def __init__(self):
        super(FlatList, self).__init__()
        self.challenge = 'Flatten a list which contains lists'

    def code(self):
        starting_list = [[1, 2, 3], [[4, 5, 6, [7, 8, 9]]]]

        print('Starting List:', starting_list)
        end_list = self.flatten_list(starting_list, 1)
        print('Flattend at 1 level:', end_list)
        end_list = self.flatten_list(starting_list, 3)
        print('Flattened fully:', end_list)

    def flatten_list(self, given_list, level=1):
        '''Flatten a list at a specified level'''
        flat = []

        to_flatten = given_list

        for i in range(0, level):
            # Reset flat per level
            flat = []
            for x in to_flatten:
                # Check if index is a list instance
                if isinstance(x, list):
                    for j in x:
                        # append elements from list
                        flat.append(j)
                else:
                    flat.append(x)

            # Set to_flatten for next loop
            to_flatten = flat

        return flat
