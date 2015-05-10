/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 *
 * @author Debaspreet Chowdhury
 */
public class heap {
    
    public int array[];
    
    public heap(){array = new int[]{4,2,7,1,9,10,20,21,32,54,34,45,67,54,87,56,45,15,100,100,32,54};}
    
    
    public void heapify()
    {
        for(int i=this.array.length;i>=2;i--)
        {
            percolate_up(i);
            percolate_down(i,this.array.length);
        }
    }
    
    
    public void percolate_up(int i)
    {
        if (this.array[i-1]>this.array[(i/2)-1])
        {
            int temp = this.array[i-1];
            this.array[i-1]=this.array[(i/2)-1];
            this.array[(i/2)-1]=temp;
        }
    }
    
    public void percolate_down(int i,int l)
    {
        if((2*i+1)<=l)
        {
            if(this.array[2*i-1]<this.array[2*i])
            {
                if(this.array[2*i]>this.array[i-1])
                {
                    int temp = this.array[2*i];
                    this.array[2*i]=this.array[i-1];
                    this.array[i-1]=temp;
                    percolate_down(2*i+1,l);
                }
            }
                else
            {
                if(this.array[2*i-1]>this.array[i-1])
                {
                    int temp = this.array[2*i-1];
                    this.array[2*i-1]=this.array[i-1];
                    this.array[i-1]=temp;
                    percolate_down(2*i,l);
                }
            }
        }
    }
    
    public void heapsort()
    {
        for(int i=this.array.length-1;i>=2;i--)
        {
            int temp=this.array[0];
            this.array[0]=this.array[i];
            this.array[i]=temp;
            percolate_down(1,i);
            this.printHeap();
        }
    }
    
    public void insert(int n)
    {
        int[] ary = new int[this.array.length + 1];
        for(int i=0;i<this.array.length;i++)
            ary[i]=this.array[i];
        ary[this.array.length]=n;
        this.array=ary;
    }
    
    public void deletemax()
    {
      //assuming the heap is heapified
        int temp=this.array[0];
        this.array[0]=this.array[array.length-1];
        this.array[array.length-1]=temp;
        percolate_down(1,this.array.length-1);
        
        int[] ary = new int[this.array.length -1];
        for(int i=0;i<this.array.length-1;i++)
            ary[i]=this.array[i];
        this.array=ary;
    }
    
    public void printHeap()
    {
        for(int i=0;i<array.length;i++)
        {
            System.out.print(array[i]+" ");
        }
        System.out.println();
    }
    
    public static void main(String[] args){
                
        heap someHeap = new heap();
        
        /**
         * print the original heap.
         */        
        System.out.println("Original array that has been inputted----->");
        someHeap.printHeap();
        System.out.println();
        
        /**
         * heapify implements percolate up and percolate down
         * results in the mximum element swim up to the top
         * of the heap.
         */
        System.out.println("Max Heapefied Heap----->");
        someHeap.heapify();
        someHeap.printHeap();
        System.out.println();
        
        /**
         *implement the actual heap sorting algorithm. 
         */
        System.out.println("Heap Sorting on Max Heap in process--------->");
        someHeap.heapsort(); 
        System.out.println();
        
        /**
         * print the final sorted array.
         */        
        System.out.println("Final Sorted out heap--------->");
        someHeap.printHeap();
        System.out.println();
        
        /**
         * Insert an element into array.Then call the heapify method
         * to heapify the array.
         */  
        System.out.println("Inserting into heap--------->");
        someHeap.insert(83);
        someHeap.printHeap();
        System.out.println();
        System.out.println("Heapefying heap just after insertion to WATCH percolation--------->");
        someHeap.heapify();
        someHeap.printHeap();
        System.out.println();
        
        /**
         * deleting the maximum from a heap and then
         * watching self percolation of elements.
         */ 
        System.out.println("Deletion of Max element from an already heapifid heap--------->");
        someHeap.deletemax();
        someHeap.printHeap();
        someHeap.deletemax();
        someHeap.printHeap();
    }
    
}
