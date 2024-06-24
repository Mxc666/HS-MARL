

(define (problem BW-rand-3)
(:domain blocksworld)
(:objects b1 b2 b3 )
(:init
(on-table b1)
(clear b1)
(on b2 b3)
(clear b3)
(on-table b3)
(on-table b3)
(on-table b2)
(clear b3)
(clear b2)
)
(:goal
(and
(on b2 b1)
(on b3 b2))
)
)
