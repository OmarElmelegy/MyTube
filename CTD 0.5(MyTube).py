import WhereAllTheMagicHappens


def main():
    while True:
        print("Welcome to MyTube..\nYou have three choices:\n1-Enter a video to search for and download\n2-Show the list of videos downloaded\n3-enter 'exit' to exit the program")
        Choice = input("Your Choice: ")
        if Choice == '1':
            Title = input("Enter what you want to search for: ")
            List = WhereAllTheMagicHappens.SearchResults(Title,10)
            for i in range(10):
                print(f"Video number {i+1}: {WhereAllTheMagicHappens.GetNames(List[i])}")
            while True:
                #try:
                    ChosenVideo = int(input("Which Video will you choose ? "))
                    if(0 < ChosenVideo <= 10):
                        LinkOfDownload = List[ChosenVideo-1]
                        Stream = WhereAllTheMagicHappens.GetResolution(LinkOfDownload)
                        WhereAllTheMagicHappens.DownloadVideo(Stream)
                        print("Video Downloaded..\n")
                        break
                    #else:
                        #raise Exception
                    #########Don't forget the break#########
                #except:
                    #print("Enter a valid number..")
        elif Choice == '2':
            WhereAllTheMagicHappens.GetVidsDownloaded()
            print("\n")
        elif Choice == 'exit':
            exit()
        else :
            print('Enter a valid choice')
    

main()