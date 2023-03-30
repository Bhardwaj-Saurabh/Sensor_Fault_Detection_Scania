# Sensor Fault Detection Using Official Scania Dataset
End to end machine learning projects based on Sensor fault detection. 

## Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air. The data set is provided by Scania with open source licence.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

As the problem is to reduce the cost due to unnecessary repairs, it is important to reduce false positives and false negatives. More importantly, to reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives as shown in [EDA](https://github.com/avnyadav/sensor-fault-detection/blob/24c6cb210619ce03f0b40eeaca167b3eb26853b8/notebooks/Scania_APS_failure_prediction.ipynb) notebook.
