
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        qk = (
            x1 @ x2.transpose(-2, -1) / torch.sqrt(x1.size(-1)) + self._attn_mask()
        )  # Compute the dot product of the query and key, scaled by the square root of the number of columns in the query tensor
        qk = qk * x3 + (x4 + 0.5) / torch.sqrt(
            x2.size(-1)
        )  # Multiply each element by 0.5; divide each element by a constant, and then compute the dot product of the result with another constant
        attn_weight = torch.softmax(qk, dim=-1)  # Compute softmax for attention weights
        attn_weight = (
            attn_weight * x3 + self._attend_dropout(attn_weight)
        )  # Apply dropout to the softmax output and multiply each element by another constant
        output = attn_weight @ x2  # Compute dot product of the attention weight with another input tensor, which is a key value pair
        return output

    def _attn_mask(self):
        attn_mask = torch.zeros((len(x1), len(x1)), device="cuda")

        for i in range(len(x1)):
            attn_mask[i][i] = float("-inf")

        return attn_mask

    def _attend_dropout(self, x):
        dropout  = torch.nn.Dropout2d()
        return dropout(x)
 
m  = Model()


# Inputs to the model
__input1__  = torch.randn(8, 3072).cuda()
__input2__  = torch.randn(4096, 128).cuda()
__output__  = m(__input1__, __input2__)

