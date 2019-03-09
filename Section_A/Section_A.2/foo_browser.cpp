#include "iostream"
#include "cstring"
using namespace std;
#define max 100

int count = -1;

class stack
{
public:
	char url[100];
}web[max];

void add(char str[]) // add url to stack
{
	count++;
	strcpy(web[count].url,str);
}

void back() // pop url
{
	count--;
}

int main()
{
	int n;
	while(count <= max)
	{
		if(count < 0)
		{
			while(n!=1) // if stack is empty
			{
				cout<<"Stack is empty press 1 enter new url"<<endl;
				cin>>n;
			}
		}
		else if(count<max)
		{
			cout<<"Press 1 to enter new url and 2 to go back"<<endl;
			cin>>n;
		}
		else
		{
			while(n!=2)
			{
				cout<<"Stack is full press 2 to go back"<<endl;
				cin>>n;
			}
		}
			
		cout<<endl;
		if(n == 1)
		{
			char str[100];
			cout<<"Enter new url"<<endl;
			cin>>str;
			add(str);
		}
		else if(n == 2)
		{
			back();
		}
		else
		{
			cout<<"Invalid Input"<<endl;
		}

		if(count == -1)
		{
			cout<<"No url present"<<endl<<endl;
		}
		else
		{
			cout<<"Welcome to "<<web[count].url<<endl<<endl;
		}
	}
}