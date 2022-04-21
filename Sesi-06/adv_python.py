# kalo dari yang dibaca sekilas, fungsi yield itu ngurangin penggunaan memori dengan cara ngebalikin generator yang dimana dia bisa di iterate lewat generator buat ngedapetin infonya
def square(nums):
    # ini salah satu contoh tempat penggunaan generator (for)
    for num in nums:
        # ini generators
        # bedany kalo python biasa pake return, ini pk yield untuk balikin nilainya
        yield (num * num)

# fyi ini di run di terminal
# intinya kalo mau run "next", varny harus di bikin itter
# nums = [1,2,3,4,5]
nums = [1,2,3,4,5].__iter__()

print(square(nums))
# ini salah satu contoh tempat penggunaan generator (next)
# ini bisanya ngerun yg ada "iter"
print(next(square(nums)))

