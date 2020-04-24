def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Moved Disk 1 from rod {} to rod {}.".format(from_rod, to_rod))
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Moved Disk {} from rod {} to rod {}.".format(n, from_rod, to_rod))
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)