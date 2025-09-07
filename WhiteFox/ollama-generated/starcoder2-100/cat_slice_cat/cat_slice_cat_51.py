
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1 = torch.cat(x, dim=1) # Concatenate the tensors along dimension 1
        size = len(t1.shape[0]) - int(np.log2(len(t1.shape[0]))) 
        t3 = t1[:, 0:size] # Slice out the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return t2
 
# Initializing the model
m = Model()

