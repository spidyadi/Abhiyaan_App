// "We're falling apart to halftime"
#include "iostream"
using namespace std;
#define max 100

int count_tube = -1, count_queue = -1;
int tube[max], queue[max];
// array tube is the tube with the dance floor
// array queue is the queue waiting to go inside the dance floor

void print() // prints all the poeple waiting in queue and inside tube
{
	cout<<endl<<"Queue: ";
	for(int i=count_queue; i>=0; i--)
		cout<<queue[i]<<' ';

	cout<<"\nTube: ";

	for(int j=count_tube; j>=0; j--)
		cout<<tube[j]<<' ';

	cout<<endl<<endl;
}

// add people either to queue or inide tube depending on fullness of tube
void add(int n) 
{
	if(count_tube < max - 1)
	{
		count_tube++;
		tube[count_tube] = n;	
	}
	else
	{
		count_queue++;
		queue[count_queue] = n;
	}
	print();
	
}

// once the buzzer is hit one person from last person from tube goes
// out and if there's a person in queue then the first person in queue
// goes in
void buzzer()
{
	if(count_queue == -1 && count_tube == -1)
	{
		cout<<"Nobody inside tube"<<endl<<endl;
		return;
	}
	else if(count_queue == -1)
	{
		count_tube--;
	}
	else
	{
		tube[max - 1] = queue[0];
		for(int i =1; i<=count_queue; i++)
			queue[i-1] = queue[i];

		count_queue--;
	}
	print();
}


int main()
{
	int n;
	while(1>0)
	{
		cout<<"Enter 1 to introduce another person or 2 to hit buzzer"<<endl;
		cin>>n;
		cout<<endl;
		if(n==1)
		{
			int ip;
			cout<<"Enter positive number"<<endl;
			cin>>ip;
			add(ip); // add person to queue or tube
		}
		else if(n==2)
		{
			buzzer(); // buzzer is hit
		}
		else
		{
			cout<<"Invalid Entry";
		}
	}
}