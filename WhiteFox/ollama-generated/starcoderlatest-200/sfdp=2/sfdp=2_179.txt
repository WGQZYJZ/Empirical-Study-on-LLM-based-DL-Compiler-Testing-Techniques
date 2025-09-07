
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) / 1000
        scaled_qk = qk.div(5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        return output
 
# Inputs to the model
query  = torch.randn(1, 8, 32, 32)
key = torch.randn(1, 8, 32, 32)
value = torch.randn(1, 8, 64, 64)
 
# Expected output:
## tensor([[104759.5332]], grad_fn=<GatherBackward>)


# Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model. The query and key should be different from the previous ones. This model requires attention.


## Output: 