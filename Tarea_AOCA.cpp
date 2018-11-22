// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    string line, originalContent = "", cleanContent = "", toBeCleaned = "", fileName = "";
    bool fileExist = false;
    cout << "Enter file name and extension (eg. example.txt): ";
    cin >> fileName;

    ifstream myfile(fileName);

    if (myfile.is_open())
    {
        while (getline(myfile, line))
        {
            originalContent += line + "\n";
            toBeCleaned += line;
        }
        myfile.close();

        for (int i = 0; i < toBeCleaned.length(); i++)
        {
            if (toBeCleaned[i] == '>' && i + 1 < toBeCleaned.length())
            {
                if (toBeCleaned[i + 1] != '<')
                {
                    for (int j = i + 1; j < toBeCleaned.length(); j++)
                    {
                        if (toBeCleaned[j] == '<')
                        {
                            i = j;
                            cleanContent += "\n";
                            break;
                        }
                        else
                        {
                            cleanContent += toBeCleaned[j];
                        }
                    }
                }
            }
        }

        cout << endl;

        cout << "Original Content: " << endl;
        cout << "------------------------------------------" << endl;
        cout << originalContent << endl;

        cout << "Clean Content: " << endl;
        cout << "------------------------------------------" << endl;
        cout << cleanContent << endl;
    }
    else
    {
        cout << "Unable to open file" << endl;
    }

    return 0;
}