from systemtools import monitoring

def main():
    print ("System CPU load is {} %".format(monitoring.Get_processorUsage()))

if __name__ == "__main__":
    main()