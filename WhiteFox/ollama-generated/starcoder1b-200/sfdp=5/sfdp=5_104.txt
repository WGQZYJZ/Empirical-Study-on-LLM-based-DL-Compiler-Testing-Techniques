
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 20)
        self.key   = torch.nn.Linear(768, 20)
        self.value = torch.nn.Linear(768, 10)
 
    def forward(self, x):
        query, key, value = (
            self.query(x[:, :768]).transpose(-2, -1),
            self.key(x[:, 768:]).transpose(-2, -1),
            self.value(x[:, 144:]).squeeze()
        )
        attn_mask = torch.unsqueeze(torch.eye(query.size(-1)).tril(), dim=1) # Transpose the attention mask so that the first column corresponds to the last column and vice-versa, which is more convenient to understand.
        return attn_weight * value  # The scaled dot product is a vector for each example.


# Initializing the model
m = Model()


