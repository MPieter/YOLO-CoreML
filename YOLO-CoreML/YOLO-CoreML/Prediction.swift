//
//  Prediction.swift
//  TinyYOLO-CoreML
//
//  Created by Pieter Meiresone on 09/09/2020.
//  Copyright © 2020 MachineThink. All rights reserved.
//

import Foundation
import CoreGraphics

struct Prediction {
    let classIndex: Int
    let score: Float
    let rect: CGRect
}
