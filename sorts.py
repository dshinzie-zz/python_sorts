from pdb import set_trace as bp

class Sort:
    def insertion_sort(self, list):
        for i in range(1, len(list)):
            x = list[i] #current placeholder
            j = i #position

            while j > 0 and list[j - 1] > x:
                list[j] = list[j - 1]
                j = j - 1

            list[j] = x

        return list

    def bubble_sort(self, list):
        swapped = True

        if len(list) <= 1:
            swapped = True

        while swapped:
            swapped = False

            for i in range(0, len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapped = True

        return list

    def merge_sort(self, list):
        if len(list) <= 1:
            return list
        middle = len(list) / 2
        return self.merger(self.merge_sort(list[:middle]), self.merge_sort(list[middle:]))

    def merger(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            elif left[0] >= right[0]:
                result.append(right.pop(0))

        if not left and len(right) > 0:
            result += right

        elif len(left) > 0 and not right:
            result += left

        return result


sort = Sort()
print sort.insertion_sort(["d", "b", "e", "a", "c"])
print sort.bubble_sort(["d", "b", "e","a", "c"])
print sort.merge_sort(["d", "b", "e", "a", "c"])
