data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=True, num_workers=1)
for (i, batch) in enumerate(loader):
    print(i, batch)
    print(torch.utils.data.get_worker_info())