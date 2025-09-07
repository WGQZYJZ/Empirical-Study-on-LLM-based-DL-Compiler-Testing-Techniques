
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
       t3  = x1.permute(0, 2, 1) # Permute the input tensor A with (1, 4, 2). In pytorch, the permute method swap the last two dimensions of the input tensor and the size is preserved
       t4  = x2.permute(0, 3, 1) # Permute the input tensor B with (1, 8, 4). In pytorch, the permute method swap the last two dimensions of the input tensor and the size is preserved
        t5 = torch.bmm(t3, t4) # The first input to this function is the permuted tensor A
       return t5
# Initializing the model