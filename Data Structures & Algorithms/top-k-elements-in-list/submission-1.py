class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
## ek empty dictionary bnai.. fir (nums) list me for loop chlaya num se iterate krakr
##count[num] se dictionary me value add hoti h mtlb count[1]=1
##toh dictionary me save hoga.. {1:1}
##count num me hmne values store krai h.. 1+ (jo b values h count me.. uspr get statement lga diya)
##or get statement ka kam h ki ye phle get(num,0) function se hmari value i.e num ise dhundega dictionary me
##agr dictionary me h toh thik h ye as it is uska index print kra dega. nhi toh default value 0 print kra dega
##isse main kam hmne kra h ki count dictionary ko fill kra h loop chla kr
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
##isse hmne main kam kra h ki array me count dictionary ki value add krai h or fir sort kra h array
##ek empty list bnai arr nam ki
##fir ek loop chlaya... for loop
##.items() se count dictionary ki sari items uthai h
##or fir iterate krakr jo b values aai h wo hmne arr me append kra di h
##fir arr sort kra h
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
##sort krne ke bad sari most repeated values h wo toh last me aa gyi na
##is liye hmne arr se pop krakr sidhha hi res me append kr diya
##hmne isme ek empty list bnai h.. jo ki jbtk k se chhota h tb tk..
##arr.pop se last element pop krega.. or res se append kr dega
## or fir last me res me aa jayenge k items.. and hence the problem solved