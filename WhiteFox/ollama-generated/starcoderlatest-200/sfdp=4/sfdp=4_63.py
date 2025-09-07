
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) # (3 x 8, ) -> 8
        self.key = torch.nn.Linear(2048, 16) # (2048, ) -> 16
 
    def forward(self, x1):
        k1 = self.query(x1).unsqueeze(-2).unsqueeze(-3) # (1 x 1, b, h, w) * (b, h, w, c_head) = (1 x b x h x w, )
        v1 = self.key(x1).unsqueeze(-2).unsqueeze(-3) # (1 x 1, h, w, 2048) * (h, w, 2048, c_head) = (1 x h x w x 2048, )
        qk = k1 @ v1.transpose(1, 2) # (1 x b x h x w, 2048 x h x w) * (h x w x 2048 x c_head, 16 x b x 1 x 1) -> (1 x b x h x w x 2048, )
        qk = qk / math.sqrt(self.query.in_features) # Scale the dot product by square-rooting the number of input features
        qk = qk + torch.eye(qk.size(-1)).unsqueeze(-3).repeat(1, 1, 2048, 1).type_as(qk) # Add an identity matrix to broadcasted the attention mask
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ v1 # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
