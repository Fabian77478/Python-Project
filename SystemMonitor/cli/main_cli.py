import systemtools.monitoring 

def main():
    print ("System CPU load is {} %".format(systemtools.monitoring.Get_processorload()))

if __name__ == "__main__":
    main()