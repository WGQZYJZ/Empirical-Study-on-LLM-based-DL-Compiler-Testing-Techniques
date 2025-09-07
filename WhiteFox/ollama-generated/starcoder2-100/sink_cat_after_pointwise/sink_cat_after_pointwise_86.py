class Model(torch.nn.Module):
    def __init__(self, n_layers=100):
        super().__init__()
        self.layers = torch.nn.Sequential()

        for i in range(n_layers + 1):
            self.layers += [torch.nn.Conv2d(3, 64, kernel_size=(7, 7)),
                            torch.nn.ReLU()]

    def forward(self, x0):
        out = x0
        for layer in self.layers:
            out = layer(out)
        return out

# Initializing the model
m = Model()


# Inputs to the model
m_inputs  = torch.randn(32, 3, 485)


# Targets of the model (for training)
m_outputs = torch.randn(32, 10)


# Training the model
optimizer  = torch.optim.SGD(m.parameters(), lr=1e-7, momentum=.9)
criterion = torch.nn.CrossEntropyLoss()

def train():
    for epoch in range(1):
        m.train()

        for data_input, target in zip(inputs, targets):
            optimizer.zero_grad()

            data_input  = data_input[0]
            output  = m(data_input)
            loss = criterion(output, target.argmax(dim=1))

            loss.backward()
            optimizer.step()
