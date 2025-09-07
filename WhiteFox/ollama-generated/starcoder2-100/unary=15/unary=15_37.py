
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
       v1  = self.conv(x1)
       v2  = torch.relu(v1)
       return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1,3,64,64)
 
__output__   = m(x1)

# A sample input to the model
input_data  = torch.tensor([[[[0.,0.], [0.,255.],[0.,0.] ]]])

import tensorflow as tf
input_tensor =  tf.Variable(tf.random.uniform((3,64,64), dtype=tf.dtypes.float32))

model_in = tf.keras.models.Sequential([
  tf.keras.layers.Conv1D(filters=8,kernel_size=(1,), padding="same",activation='relu',input_shape=[None, 64])],
)

model_out = model_in(input_tensor).numpy()

