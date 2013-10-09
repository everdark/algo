* RATS code
* given a 3-dimensional array, or a stack of matrices
* this algorithm sorts each matrix along the third dimension via insertion sort in replace,
* by comparing the first element (look rightward only when there is a tie)

function tensor_sort tensor

type vect[rect] tensor_sort *tensor
local int tensor_size i j optimal p q row_len col_len found_smaller found_diff
local rect rect_temp

compute tensor_size = %rows(tensor)
compute row_len = %rows(tensor(1))
compute col_len = %cols(tensor(1))

if tensor_size < 2 {
    return
}

do i = 1, tensor_size

* find the smallest matrix from i+1 to tensor_size as j
compute optimal = i
compute found_smaller = 0

do j = i + 1, tensor_size

* if j < optimal, then assign optimal to j
compute found_diff = 0
do p = 1, row_len
do q = 1, col_len
if tensor(j)(p, q) <> tensor(optimal)(p, q) {
    compute found_diff = 1
    if tensor(j)(p, q) < tensor(optimal)(p, q) {
        compute optimal = j
        compute found_smaller = 1
    }
    break
}
end do q
if found_diff == 1 {
    break
}
end do p

end do j

*swap i and optimal(the current j)
if found_smaller == 1 {
    compute rect_temp = tensor(i)
    compute tensor(i) = tensor(optimal)
    compute tensor(optimal) = rect_temp
}

end do i

end

compute null = tensor_sort(tensor)
dis tensor