DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)  # <1>
print('d1:', d1.keys())

d2 = dict(sorted(DIAL_CODES))  # <2>
print('d2:', d2.keys())

d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))  # <3>
print('d3:', d3.keys())

print('d1 == d2 and d2 == d3:', d1 == d2 and d2 == d3)
assert d1 == d2 and d2 == d3