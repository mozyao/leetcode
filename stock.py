def maxProfit(prices):
    ans=0
    if len(prices) == 0:
        return ans
    low_point = prices[0]
    for i in range(1,len(prices)-1):

        
        if prices[i]>low_point:
            profits=prices[i]-low_point
            ans=max(ans,profits)
            
        else:
            low_point = prices[i]



          
    return ans




def main():
    ans =  maxProfit([7,1,5,3,6,4])
    print("myans is : ",ans)

if __name__ == "__main__":
    main()



