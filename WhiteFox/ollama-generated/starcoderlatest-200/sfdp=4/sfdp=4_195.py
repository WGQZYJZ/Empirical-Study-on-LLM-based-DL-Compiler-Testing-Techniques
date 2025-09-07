
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 3)
        self.key = torch.nn.Linear(256, 3)
        self.value = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        qk = torch.bmm(
            (
                (
                    (
                        self.query(x1)
                    )
                ).transpose(-2, -1) # Convert the input to a form suitable for the matrix multiplication
            ),
            (
                (
                    (
                        self.key(x1).transpose(-2, -1)
                    )
                )
            ),
        ) / math.sqrt(256) # Scale the dot product by dividing it by its square root

        attn_mask = torch.zeros((qkv.shape[0], qkv.shape[0])).float().cuda()

        if attn_mask.is_cuda:
            attn_mask.data.fill_(1 - self._epsilon)

        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Scale the dot product by dividing it by its square root
        output = torch.bmm(attn_weight, (self.value(x1)))

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 256, 40).cuda() # [B, D, L]
