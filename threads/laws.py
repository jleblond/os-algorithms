
def amdahls_law(s, n):
    """
    Amdahl's Law
    Identifies performance gains from adding additional cores to an application that has both serial and parallel components.
    Serial portion of an application has disproportionate effect on performance gained by adding additional cores
    :param s: serial portion (% of serial portions in the app, value format ranging from 0.0 to 1.0)
    :param n: processing cores
    :return: speed_up
    """
    speed_up = 1/(s+((1-s)/n))
    print("speedup <= " + str(speed_up))
    print("That is, if application is " + str((1-s)*100) + "% parallel / " + str(s*100) + "% serial, "
           "moving from 1 to " + str(n) + " cores results in speedup of " + str(speed_up) + ' times')
    return speed_up
