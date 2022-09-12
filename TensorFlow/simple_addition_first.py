# addition using tensorflow
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# creating nodes in computation graph
node1 = tf.constant(3, dtype=tf.int32)
node2 = tf.constant(5, dtype=tf.int32)
node3 = tf.add(node1, node2)
node4 = tf.multiply(node1, node2)

with tf.Session() as sess:
    print("Product of node1 and node2 is:",sess.run(node4))

# create tensorflow session object
sess = tf.Session()
print("Sum of node1 and node2 is:", sess.run(node3))

# closing the session is not necessary with loop method
sess.close()
