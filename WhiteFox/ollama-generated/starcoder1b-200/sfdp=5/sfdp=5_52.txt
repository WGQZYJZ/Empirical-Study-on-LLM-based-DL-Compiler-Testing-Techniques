
class Model(torch.nn.Module):
    def __init__(self, input_dim=None, hid_dim=None, drop_rate=0.25):
        super().__init__()
        self.attn = torch.nn.Linear(input_dim, hid_dim, bias=True)
        self.layer1 = torch.nn.Linear(hid_dim, hid_dim, bias=True)
        self.layer2 = torch.nn.Linear(hid_dim, input_dim, bias=False)
        self.drop = torch.nn.Dropout(p=drop_rate)
 
    def forward(self, x):
        # Compute the attention weights
        qk = self.attn(x).transpose(-1, -2)  # Compute the dot product of the query and key (plus an attention mask)
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result (and scale)
        # Dropout the output to avoid overfitting
        x = self.drop(attn_weight @ x)
        x = self.layer1(x)
        x = self.layer2(x)
        return x


# Initializing the model
m = Model()

