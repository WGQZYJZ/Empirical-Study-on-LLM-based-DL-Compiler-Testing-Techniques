
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.ops._caffe2.mkldnnbenchmark_matmat_mk2_op(3, 4)
 
    def forward(self, x1, y1, z1, k1):
        v1  = self.mm(x1, y1, z1, k1) 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 50000).numpy().astype('float32')
y1  = torch.randn(4, 70000).numpy().astype('float32')
z1  = torch.randn(3, 60000).numpy().astype('float32')
k1  = np.array([5], dtype='int32')


__output__  = m(x1, y1, z1, k1) 

