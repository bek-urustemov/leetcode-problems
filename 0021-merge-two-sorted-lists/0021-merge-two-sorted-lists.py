class Solution:
    def mergeTwoLists(self, list1, list2):

        pointer_1 = list1
        pointer_2 = list2

        new_list = ListNode()
        current = new_list

        while pointer_1 and pointer_2:

            if pointer_1.val > pointer_2.val:
                current.next = pointer_2
                pointer_2 = pointer_2.next
            else:
                current.next = pointer_1
                pointer_1 = pointer_1.next

            current = current.next

        if pointer_1:
            current.next = pointer_1

        if pointer_2:
            current.next = pointer_2

        return new_list.next