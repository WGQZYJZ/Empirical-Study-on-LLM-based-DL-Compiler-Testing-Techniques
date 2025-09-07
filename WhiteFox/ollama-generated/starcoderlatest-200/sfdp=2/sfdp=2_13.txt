
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 512)
        self.fc2 = torch.nn.Linear(512, 256)
 
    def forward(self, x1):
        v1 = torch.tanh(self.fc1(x1)) # Compute the tanh of the output of fc1
        v2 = torch.tanh(self.fc2(v1)) # Compute the tanh of the output of fc2
        v3 = torch.matmul(v2, self.key_weight) + self.query_bias
        softmax_v4 = nn.functional.softmax(v3, dim=-1) # Apply softmax to the output of matmul
        dropout_v5 = nn.functional.dropout(softmax_v4, p=dropout_p) # Apply dropout to the softmax output
        v6 = dropout_v5.matmul(self.value_weight) + self.value_bias
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2048, 1, 1)
