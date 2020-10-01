#include <iostream>
#include <algorithm>
using namespace std;

class Job{
    public:
    int id,time,value;
    Job(int id,int time,int value)
    {
     this->id=id;
     this->time=time;
     this->value=value;
    }
};

bool comparison(Job *a,Job *b)
{
    return(a->value>b->value);
}
int main() {
	int t=1;
	cin>>t;
	while(t--)
	{
	  int n;
	  cin>>n;
	  Job *ptr[n];
	  for(int i=0;i<n;i++)
	  {
	      int a,b,c;
	      cin>>a>>b>>c;
	      ptr[i]=new Job(a,b,c);
	      
	  }
	  sort(ptr,ptr+n,comparison);
     
	  vector<bool> free(n,true);
	  int profit=0,jobs=0;
      
      for(int i=0;i<n;i++)
      {
          for(int j=ptr[i]->time-1;j>=0;j--)
          {
              if(free[j])
              {
                  free[j]=false;
                  profit+=ptr[i]->value;
                  jobs++;
                  break;
              }
          }
      }
	  cout<<jobs<<" "<<profit<<endl;
	  
	return 0;
	}
}
