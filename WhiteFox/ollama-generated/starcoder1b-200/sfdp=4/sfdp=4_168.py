
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and key tensors,
        # scale it, and add the attention mask to the result
        qk = self.conv(x1) @ torch.tanh(x2 / math.sqrt(x1.size(-1))) + 1e-8
        # Scale the attention weights using softmax
        attn_weight = nn.Softmax(dim=-1)(qk)
        # Compute the dot product of the attention weights and value, 
        # and then scale it back to unscale the dot products 
        # that are multiplied by the attention masks for each head
        output = torch.bmm(attn_weight, x2)
        return output


# Initializing the model
m = Model()


