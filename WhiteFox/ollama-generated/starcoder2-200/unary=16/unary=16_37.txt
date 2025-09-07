
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 5)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.relu(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(32, 50*784)
 
 # Initializing the data loaders. The number of workers is set to zero because we want to run this notebook on Google Colab. If you are using PyTorch for the first time in your machine and you are getting OOM (out-of-memory error), try reducing the batch size or number of workers accordingly.
 dl_train  = torch.utils.data.DataLoader(dataset=MNISTDataset('train', transform='toTensor'),
                                          batch_size=32, shuffle=True)
 dl_test   = torch.utils.data.DataLoader(dataset=MNISTDataset('test',  transform='toTensor'),
                                         batch_size=32, shuffle=True)
  # Model training. For simplicity reasons we will use the CPU to run this notebook and for model training on a GPU machine you would need to replace 'cpu' with 'cuda' in the line where you initialize your device.
 num_epochs  =  10
 train(m, dl_train, dl_test, num_epochs=num_epochs)

