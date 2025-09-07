
class Model(torch.nn.Module):
    def __init__(self, input_size=20):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_size, 5)
        self.fc2 = torch.nn.Linear(5, 2)
 
    def forward(self, x):
        q = self.fc1(x)
        key = self.fc2(q)
        attn_weight = self.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        value = self.linear(x)
        output = attn_weight @ value

# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(100, 20)
