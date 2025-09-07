
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.functional.dropout(
            torch.rand(1, 2, 3), 
            p=0.25, 
            training=training)
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.relu(
            self.dropout1)  # Apply dropout to the input tensor, or a node invoking it will be erased from the graph by the `replace_fx` optimization above
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
