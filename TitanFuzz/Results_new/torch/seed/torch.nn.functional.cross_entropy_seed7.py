batch_size = 5
num_classes = 2
num_inputs = 10
np.random.seed(42)
input = np.random.randn(batch_size, num_inputs)
target = np.random.randint(num_classes, size=(batch_size,))
input = torch.from_numpy(input).float()
target = torch.from_numpy(target).long()
output = torch.nn.functional.cross_entropy(input, target)