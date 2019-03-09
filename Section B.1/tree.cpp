#include "iostream"
#include "cstdlib"
using namespace std;

int index_parent; // index of the parent node at any point in time
int index_total; // total no. of nodes at any point of time - 1
class node
{
public:
	int value; // value of node
	int index_p; // parent index of node
	int index; //  index of node
	int index_d[10]; //  daughter indices of node
	int count_d; // count of no. of daughter nodes
	node()
	{
		count_d = -1;
		index_p = -1;
	}
	void create(int v, int p, int i) // creates node
	{
		value = v;
		index_p = p;
		index = i;
	}
	void daught(int i) // adds daughter node
	{
		count_d++;
		index_d[count_d] = i;
	}
}array_of_nodes[50];

void branch(char *str, int i) // add daughter nodes to cuurent parent node
{
	index_total++;
	int v;
	if(str[i+1]-'0' <=9 && str[i+1]-'0' >=0)
	{
		v = 10*(str[i] - '0') + (str[i+1] - '0');
		i++;
	}
	else
		v = str[i] -'0';

	array_of_nodes[index_total].create(v, index_parent, index_total);
	array_of_nodes[index_parent].daught(index_total);
	// if next char in str is an open bracket the daughter node 
	// becomes the parent node
	if(str[i+1] == '[')
	{
		index_parent = index_total;
	}
}

// when a clode bracket is encountered
void close()
{
	index_parent = array_of_nodes[index_parent].index_p;
}

// printing the tree with root as max_index
void root(int max_index)
{
	int x = 0;
	for(int i=max_index; i<=index_total; i++)
	{
		for(int j=0; j<=array_of_nodes[i].count_d; j++)
		{
			x = 1;
			cout<<array_of_nodes[i].value<<"-->"<<array_of_nodes[array_of_nodes[i].index_d[j]].value<<endl;
		}
	}

	if(x==0)
		cout<<"Cannot build tree with root as "<<array_of_nodes[max_index].value<<endl;
}

int main()
{
	char str[100];
	cin>>str;
	for(int i=0; str[i]!='\0'; i++)
	{
		if(i==0)
		{
			int v;
			if(str[i+1]-'0' <=9 && str[i+1]-'0' >=0)
				v = 10*(str[i] - '0') + (str[i+1] - '0');
			else
				v = str[i] -'0';
			array_of_nodes[0].create(v,-1,0);

			index_parent = 0;
			index_total = 0;
			i++;
		}

		if(str[i] == '[' || str[i] == ',')
		{
			branch(str, i+1);
		}
		else if(str[i] == ']')
		{
			close();
		}
	}
	
	for(int i=0; i<=index_total; i++)
	{
		for(int j=0; j<=array_of_nodes[i].count_d; j++)
		{
			cout<<array_of_nodes[i].value<<"-->"<<array_of_nodes[array_of_nodes[i].index_d[j]].value<<endl;
		}
	}

	cout<<endl<<"Right View: "<<'[';
	int i,max=0, max_index;
	for(i=0; array_of_nodes[i].count_d >= 0; )
	{
		cout<<array_of_nodes[i].value<<", ";

		i = array_of_nodes[i].index_d[array_of_nodes[i].count_d];

		if(array_of_nodes[i].value > max)
		{
			max = array_of_nodes[i].value;
			max_index = i;
		}
	}
	cout<<array_of_nodes[i].value<<']'<<endl;

	cout<<"argmax(right_view): "<<max<<endl<<endl;
	root(max_index);
}