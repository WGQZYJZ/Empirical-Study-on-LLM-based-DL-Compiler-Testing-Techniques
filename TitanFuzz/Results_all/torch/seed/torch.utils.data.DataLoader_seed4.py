input_data = torch.rand(10, 3)
target_data = torch.rand(10)
dataset = torch.utils.data.TensorDataset(input_data, target_data)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True)
for (batch_index, (input_data, target_data)) in enumerate(dataloader):
    print('batch_index: ', batch_index)
    print('input_data: ', input_data)
    print('target_data: ', target_data)
    print('\n')