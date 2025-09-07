
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(768, 10)
 
    def forward(self, x, key=None, attn_mask=None):
        qkv = self.fc(x).chunk(3, dim=-1)  # Split the input tensor into a batch of three columns: head, query and key.
        k, v = qkv[0], qkv[1]  # Extract the query and key tensors from the list `qkv` (that's why they are in reversed order)
        attn_weight = torch.softmax(k @ v.transpose(-2, -1) / math.sqrt(key.size(-1)), dim=-1)  # Compute the dot product of the attention weights and the value
        output = self.fc(attn_weight @ v).chunk(3, dim=-1)  # Split the weighted sum from the list `output` (that's why they are in reversed order)
        output = torch.cat([o * attn_mask[:, :, None] for o in output], dim=-2)  # Compute the input tensor after the weighted sum is applied to it.
        return output[0].squeeze(-1)


# Initializing the model
m = Model()
m.__repr__()  # Print the representation of the model


