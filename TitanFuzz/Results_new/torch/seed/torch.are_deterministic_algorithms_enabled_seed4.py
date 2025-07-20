batch_size = 256
train_dataset = MNIST(root='../../data', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = MNIST(root='../../data', train=False, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
torch.are_deterministic_algorithms_enabled()