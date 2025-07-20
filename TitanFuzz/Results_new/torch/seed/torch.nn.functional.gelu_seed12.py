input = np.array([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
input = torch.tensor(input, dtype=torch.float32)
output = torch.nn.functional.gelu(input)