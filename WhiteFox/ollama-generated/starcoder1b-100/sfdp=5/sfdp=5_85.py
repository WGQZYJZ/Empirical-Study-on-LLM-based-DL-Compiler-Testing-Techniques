
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        self.transformer = Transformer(args)
 
    def forward(self, x1, x2):
        # Step 1: Calculate the query, key, value and attention mask
        qk, attn_mask = self.transformer(x1, x2)
        # Step 2: Apply dropout to compute the output
        output = qk @ attn_weight * value
        return output


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
x2  = torch.randn(3, 8, 64, 64)
