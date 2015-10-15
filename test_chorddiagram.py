#!usr/bin/env python3
import unittest
import chorddiagram as cd
from chorddiagram import String, Dot


class TestChorddiagram(unittest.TestCase):

  def test_init(self):
    """
    Struggling to write good tests here 

    """
    d = cd.ChordDiagram()
    #d.show()


    d.draw()
    self.assertTrue(d.string_top < d.string_bottom)

    #Check frets are not on top of each other
    fret_y = 0
    for f in d.frets:
      self.assertTrue(f.y > fret_y)
      fret_y = f.y
      
    #'Normal' chord, diagram should have 5 frets
    self.assertEqual(d.num_frets, 5)

   
      
    d= cd.ChordDiagram( name="D", strings=[String([Dot(2,1)]),String([Dot(2,1)]),String([Dot(2,1)]),String([Dot(5, 3),Dot(2,1)])])
    #d.show()

    
    d= cd.ChordDiagram( name="G", strings=[String([Dot(0)]),String([Dot(2,1)]),String([Dot(3,3)]),String([Dot(2, 2)])])
    d.draw()

    #Guitar G chord
    d= cd.ChordDiagram( name="G", strings=[String([Dot(3,2)]),String([Dot(2,1)]),String([Dot(0)]),String([Dot(0)]),String([Dot(0)]), String([Dot(3,3)])])
    #Check strings are not on top of each other
   
    
    d.draw()
    self.assertEqual(d.num_strings, 6)
    string_x = 0
    for s in d.strings:
      self.assertTrue(s.string_x > string_x)
      string_x = s.string_x
      self.assertTrue(string_x < cd.ChordDiagram.box_width)

  def test_parse(self):
        #Simple chord
        achord = "{define: A frets 2 1 0 0}"
        d = cd.ChordDiagram()
        d.parse_definition(achord)
        d.draw()
        self.assertEqual(d.num_strings, 4)
        self.assertEqual(d.strings[0].dots[0].fret, 2)
        self.assertEqual(d.strings[0].dots[0].finger, None)
        self.assertEqual(d.strings[1].dots[0].fret, 1)
        self.assertEqual(d.strings[1].dots[0].finger, None)
        self.assertEqual(d.strings[2].dots[0].fret, 0)
        self.assertEqual(d.strings[2].dots[0].finger, None)
        self.assertEqual(d.strings[3].dots[0].fret, 0)
        self.assertEqual(d.strings[3].dots[0].finger, None)
        
        # Simple chord without "frets"
        achord = "{define: A 2 1 0 0}"
        d = cd.ChordDiagram()
        d.parse_definition(achord)
        d.draw()
        self.assertEqual(d.num_strings, 4)
        self.assertEqual(d.strings[0].dots[0].fret, 2)
        self.assertEqual(d.strings[0].dots[0].finger, None)
        self.assertEqual(d.strings[1].dots[0].fret, 1)
        self.assertEqual(d.strings[1].dots[0].finger, None)
        self.assertEqual(d.strings[2].dots[0].fret, 0)
        self.assertEqual(d.strings[2].dots[0].finger, None)
        self.assertEqual(d.strings[3].dots[0].fret, 0)
        self.assertEqual(d.strings[3].dots[0].finger, None)
        
        # Chord with fingering
        achord = "{define: A frets 2 1 0 0 fingers 2 1 0 0}"
        d = cd.ChordDiagram()
        d.parse_definition(achord)
        d.draw()
        self.assertEqual(d.num_strings, 4)
        self.assertEqual(d.strings[0].dots[0].fret, 2)
        self.assertEqual(d.strings[1].dots[0].fret, 1)
        self.assertEqual(d.strings[2].dots[0].fret, 0)
        self.assertEqual(d.strings[3].dots[0].fret, 0)

        
        # Chord with added fingering
        aaugchord = "{define: Aaug frets 2 1 1 4 fingers 2 1 1 4 add: string 1 fret 1 finger 1 add: string 4 fret 1 finger 1}"
        d = cd.ChordDiagram()
        d.parse_definition(aaugchord)
        d.show()
        self.assertEqual(d.num_strings, 4)
        # Chord starting on a higher fret


        # Chord with non-played strings

      

if __name__ == '__main__':
    unittest.main()