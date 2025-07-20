x = torch.tensor([(- 1.0), 1.0, 2.0])
y = torch.nn.functional.sigmoid(x)
z = torch.nn.functional.relu(x)
a = torch.nn.functional.tanh(x)